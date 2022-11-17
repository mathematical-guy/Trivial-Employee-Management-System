<template>
  <v-dialog v-model="dialog" width="400">
    <template v-slot:activator="{ on, attrs }">
      <v-btn dark v-bind="attrs" v-on="on" class="red" slot="activator">
        <v-icon>delete</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-form>
        <v-container>
          <v-row
            ><h2 class="mt-4 mb-8 ml-4">
              Delete this Employee {{ id }} ?
            </h2></v-row
          >
          <v-btn dark class="mr-5 sm" @click="deleteEmployee">Yes</v-btn>
          <v-btn @click="dialog = false">Cancel</v-btn>
        </v-container>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import { deleteEmployeeAPI } from "../services/api";
export default {
  name: "DeleteEmployeeDialog",
  props: ["id"],
  data() {
    return {
      success_message: 'Employee deleted successfully !',
      dialog: false,
      snackBarColor: "blue-grey darken-3",
    };
  },
  methods: {
    deleteEmployee() {
      deleteEmployeeAPI(this.id)
        .then((res) => {
          this.dialog = false;
          this.$emit('refreshList', res)
          this.$emit("showSnackBar", {
            message: this.success_message,
            snackBarColor: this.snackBarColor
            });
        })
        .catch((error) => console.error(error));
    },
  },
};
</script>

<style>
body {
  overflow: hidden;
}
</style>