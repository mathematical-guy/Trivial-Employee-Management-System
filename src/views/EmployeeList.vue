<template>
  <div>
    <AddEmployeeFormDialog
      @refreshList="getEmployees"
      @showSnackBar="showSnackBar"
    />
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Update</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td>{{ employee.id }}</td>
          <td>{{ employee.employee_first_name }}</td>
          <td>{{ employee.employee_last_name }}</td>
          <td>
            <v-row class="py-3">
              <EditFormDialog
                class="mx-3"
                @refreshList="getEmployees"
                :id="employee.id"
                @showSnackBar="showSnackBar"
              />
              <DeleteEmployeeDialog
                @refreshList="getEmployees"
                :id="employee.id"
                @showSnackBar="showSnackBar"
              />
            </v-row>
          </td>
        </tr>
      </tbody>
    </table>
    <SuccessSnackBar
      class="red"
      :isDisplaySnackBar="isDisplaySnackBar"
      :message="message"
      :snackBarColor=snackBarColor
    />
  </div>
</template>

<script>
import { getEmployeesList } from "../services/api";
import EditFormDialog from "../components/EditFormDialog.vue";
import AddEmployeeFormDialog from "../components/AddEmployeeFormDialog.vue";
import DeleteEmployeeDialog from "../components/DeleteEmployeeDialog.vue";
import SuccessSnackBar from "../components/SuccessSnackBar.vue";

export default {
  name: "EmployeeList",
  components: {
    EditFormDialog,
    AddEmployeeFormDialog,
    DeleteEmployeeDialog,
    SuccessSnackBar,
  },
  data() {
    return {
      message: "",
      employees: [],
      error: "",
      isDisplaySnackBar: false,
      snackBarColor: ""
    };
  },
  methods: {
    resetPage() {
      this.message = "";
      this.error = "";
      this.isDisplaySnackBar = false;
    },
    getEmployees() {
      getEmployeesList()
        .then((response) => {
          this.employees = response.data;
        })
        .catch((error) => {
          this.error = error;
          console.error(error);
        });
        this.resetPage();
    },
    showSnackBar(obj) {
      this.isDisplaySnackBar = true;
      this.message = obj.message;
      this.snackBarColor = obj.snackBarColor
    },
  },
  mounted() {
    this.resetPage();
    this.getEmployees();
  },
};
</script>

<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>