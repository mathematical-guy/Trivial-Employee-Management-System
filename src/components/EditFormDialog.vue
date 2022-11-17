<template>
  <div>
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          dark
          v-bind="attrs"
          v-on="on"
          class="green"
          slot="activator"
          @click="getEmployeeDetails(id)"
        >
          <v-icon>mode_edit</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-form>
          <v-container>
            <v-row class="mt-1 ml-1">Employee ID: {{ id }}</v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="first_name"
                  label="First name"
                  required
                ></v-text-field>
              </v-col>

              <v-col>
                <v-text-field
                  v-model="last_name"
                  label="Last name"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                ><v-btn class="success" @click="updateEmployee(id)"
                  >Submit</v-btn
                ></v-col
              >
            </v-row>
          </v-container>
        </v-form>
      </v-card>
    </v-dialog>
  </div>
</template>



<script>
import { fetchEmployeeAPI, updateEmployeeAPI } from "../services/api";
export default {
  name: "EditFormDialog",
  props: ["id"],
  data() {
    return {
      dialog: false,
      first_name: "",
      last_name: "",
      success_message: "Employee details updated successfully !",
      snackBarColor: "green lighten-1",
    };
  },
  methods: {
    getEmployeeDetails(id) {
      fetchEmployeeAPI(id, { hello: "world" })
        .then((res) => {
          this.first_name = res.data.employee_first_name;
          this.last_name = res.data.employee_last_name;
        })
        .catch((error) => console.error(error));
    },
    updateEmployee(id) {
      updateEmployeeAPI(id, {
        employee_first_name: this.first_name,
        employee_last_name: this.last_name,
      })
        .then((res) => {
          this.dialog = false;
          this.$emit("refreshList", res);
          this.$emit("showSnackBar", {
            message: this.success_message,
            snackBarColor: this.snackBarColor,
          });
        })
        .catch((error) => console.error(error));
    },
  },
};
</script>

<style>
</style>