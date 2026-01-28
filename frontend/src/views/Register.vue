<template>
  <a-row justify="center" align="middle" style="height: 100vh">
    <a-col :span="8">
      <a-card title="Register">
        <a-form :model="form" @finish="onSubmit">
          <a-form-item name="first_name" label="First Name">
            <a-input v-model:value="form.first_name" />
          </a-form-item>

          <a-form-item name="last_name" label="Last Name">
            <a-input v-model:value="form.last_name" />
          </a-form-item>

          <a-form-item name="email" label="Email">
            <a-input v-model:value="form.email" />
          </a-form-item>

          <a-form-item name="password" label="Password">
            <a-input-password v-model:value="form.password" />
          </a-form-item>

          <a-button type="primary" html-type="submit" block>
            Register
          </a-button>
        </a-form>

        <div style="margin-top: 12px; text-align: center">
          <a @click="$router.push('/login')">Back to login</a>
        </div>
      </a-card>
    </a-col>
  </a-row>
</template>

<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import { reactive } from "vue";

const router = useRouter();

const form = reactive({
  first_name: "",
  last_name: "",
  email: "",
  password: "",
});

const onSubmit = async (values) => {
  try {
    await axios.post("http://localhost:8000/auth/register", values);
    router.push("/login");
  } catch (e) {
    alert("Registration failed");
  }
};
</script>
