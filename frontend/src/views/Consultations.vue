<template>
  <a-card>
    <template #title>
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <span>Past Consultations</span>
        <a-button type="primary" @click="showModal = true">Add</a-button>
      </div>
    </template>

    <a-table 
      :columns="columns" 
      :data-source="data" 
      :row-key="record => record.id"
      :pagination="pagination"
      :loading="loading"
      @change="handleTableChange"
    />

    <!-- Modal -->
    <a-modal v-model:visible="showModal" title="New Consultation" destroy-on-close :footer="null">
      <a-form
        ref="formRef"
        :model="form"
        @finish="onSubmit"
        layout="vertical"
      >
        <a-form-item
          label="Patient Name"
          name="patient_name"
          :rules="[{ required: true, message: 'Please enter patient name' }]"
        >
          <a-input v-model:value="form.patient_name" />
        </a-form-item>

        <a-form-item
          label="Description"
          name="notes"
          :rules="[{ required: true, message: 'Please enter description' }]"
        >
          <a-input v-model:value="form.notes" />
        </a-form-item>

        <a-form-item
          label="Diagnosis Code"
          name="diagnosis_code_id"
          :rules="[{ required: true, message: 'Please select diagnosis code' }]"
        >
          <a-select
            v-model:value="form.diagnosis_code_id"
            show-search
            placeholder="Search diagnosis code"
            :options="diagnosisOptions"
            :filter-option="false"
            :not-found-content="diagnosisLoading ? 'Searching...' : 'No results'"
            @search="onDiagnosisSearch"
          />
        </a-form-item>

        <a-form-item>
          <a-button type="primary" html-type="submit" block :loading="saving">Save</a-button>
        </a-form-item>
      </a-form>
    </a-modal>
  </a-card>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import { format } from 'date-fns';
import api from "../api/http";

const data = ref([]);
const showModal = ref(false);
const formRef = ref();
const saving = ref(false);
const loading = ref(false);

// Pagination state
const pagination = reactive({
  current: 1,
  pageSize: 10,
  total: 0,
  showSizeChanger: true,
  showQuickJumper: true,
  showTotal: (total, range) => `Showing ${range[0]}-${range[1]} of ${total} items`,
  pageSizeOptions: ['10', '20', '50', '100']
});

const diagnosisOptions = ref([]);
const diagnosisLoading = ref(false);
let searchTimeout = null;

const form = reactive({
  patient_name: "",
  diagnosis_code_id: "",
  notes: ""
});

const columns = [
  { title: "Patient", dataIndex: "patient_name" },
  { 
    title: "Diagnosis", 
    customRender: ({ record }) => {
      if (record.diagnosis_code && record.description) {
        return `${record.diagnosis_code} (${record.description})`;
      }
      if (record.diagnosis_code) {
        return record.diagnosis_code;
      }
      return '-';
    }
  },
  { title: "Notes", dataIndex: "notes", ellipsis: true },
  { 
    title: "Date", 
    dataIndex: "created_at",
    customRender: ({ text }) => {
      if (!text) return '-';
      return format(new Date(text), 'yyyy-MM-dd');
    }
  }
];

const fetchConsultations = async (page = 1, pageSize = 10) => {
  try {
    loading.value = true;
    const res = await api.get("/consultation", {
      params: {
        page: page,
        page_size: pageSize
      }
    });
    
    // Handle both response structures
    if (res.data.data && res.data.pagination) {
      // New structure with pagination metadata
      data.value = res.data.data;
      pagination.total = res.data.pagination.total;
      pagination.current = res.data.pagination.page;
    }
    
  } catch (error) {
    console.error("Error fetching consultations:", error);
  } finally {
    loading.value = false;
  }
};

const handleTableChange = (newPagination) => {
  fetchConsultations(newPagination.current, newPagination.pageSize);
};

const onDiagnosisSearch = (query) => {
  if (searchTimeout) clearTimeout(searchTimeout);
  if (!query) {
    diagnosisOptions.value = [];
    return;
  }

  searchTimeout = setTimeout(async () => {
    diagnosisLoading.value = true;
    try {
      const res = await api.get("/diagnosis", { params: { search: query } });
      diagnosisOptions.value = res.data.map(d => ({
        label: `${d.code} - ${d.description}`,
        value: d.id
      }));
    } catch (error) {
      console.error("Error fetching diagnosis:", error);
    } finally {
      diagnosisLoading.value = false;
    }
  }, 400);
};

const onSubmit = async (values) => {
  try {
    saving.value = true;
    await api.post("/consultation", values);
    showModal.value = false;
    
    // Reset form
    formRef.value.resetFields();
    
    // Refresh data - go back to first page after adding new record
    fetchConsultations(1, pagination.pageSize);
    
  } catch (error) {
    console.error("Error saving consultation:", error);
  } finally {
    saving.value = false;
  }
};

onMounted(() => {
  fetchConsultations(1, pagination.pageSize);
});
</script>