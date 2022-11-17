<template>
  <v-dialog v-model="dialog" width="800">
    <template v-slot:activator="{ on, attrs }">
      <v-row>
        <v-spacer></v-spacer>
        <v-btn
          dark
          v-bind="attrs"
          v-on="on"
          class="blue mb-5 mr-10"
          slot="activator"
          @click="resetForm"
          ><b>Add Employee</b>
          <v-icon>add</v-icon>
        </v-btn>
      </v-row>
    </template>

    <v-card>
      <v-form>
        <v-container>
          <v-row class="mt-1 ml-1"
            ><strong>Enter new employee details: </strong></v-row
          >
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
              ><v-btn class="success" @click="addEmployee">Submit</v-btn></v-col
            >
          </v-row>
        </v-container>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import { createEmployeeAPI } from "../services/api";
export default {
  name: "AddEmployeeFormDialog",
  emits: ["refreshList", "showSnackBar"],
  data() {
    return {
      dialog: false,
      snackbar: false,
      first_name: "",
      last_name: "",
      success_message: "Employee Added Successfully !",
      snackBarColor: "green lighten-1"
    };
  },
  methods: {
    addEmployee() {
      createEmployeeAPI({
        employee_first_name: this.first_name,
        employee_last_name: this.last_name,
      })
        .then((res) => {
          this.dialog = false;
          this.$emit("refreshList", res);
          this.$emit("showSnackBar", {
            message: this.success_message,
            snackBarColor: this.snackBarColor
            });
        })
        .catch((err) => console.error(err));
    },
    resetForm() {
      this.first_name = "";
      this.last_name = "";
    },
  },
};
</script>

<style>
</style>