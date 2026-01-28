<template>
  <a-row justify="center" align="middle" style="height: 100vh">
    <a-col :span="8">
      <a-card title="ClinicCare Login">
        <a-form :model="form" @finish="onSubmit">
            
          <a-form-item name="email" label="Email">
            <a-input v-model:value="form.email" placeholder="Email" />
          </a-form-item>

          <a-form-item name="password" label="Password">
            <a-input-password
              v-model:value="form.password"
              placeholder="Password"
            />
          </a-form-item>

          <a-button type="primary" html-type="submit" block> Login </a-button>
        </a-form>

        <div style="margin-top: 12px; text-align: center">
          <a @click="$router.push('/register')">Register now</a>
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
  email: "",
  password: "",
});

const onSubmit = async (values) => {
  try {
    console.log("Calling!!!");
    const res = await axios.post("http://localhost:8000/auth/login", values);

    localStorage.setItem("access_token", res.data.access_token);
    localStorage.setItem("refresh_token", res.data.refresh_token);
    router.push("/consultations");
  } catch (e) {
    alert("Invalid credentials");
  }
};
</script>
