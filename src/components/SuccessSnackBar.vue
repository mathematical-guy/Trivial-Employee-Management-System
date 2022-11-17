<template>
  <div class="text-center">
    <v-snackbar
      v-model="isSnackBarDisplayed"
      top
      :color=snackBarColor
      :timeout="timeout"
    >
      <span width="100">{{ message }}</span>
      <v-btn text class="ml-16" @click="isSnackBarDisplayed = false">
        <v-icon>cancel</v-icon>
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  name: "SuccessSnackBar",
  props: {
    message: {
      type: String,
      default: "Operation Successful!",
      required: false,
    },
    isDisplaySnackBar: Boolean,
    snackBarColor: {
        type: String,
        default: "green lighten-1"
    }
  },
  data() {
    return {
      timeout: 3000,
      isSnackBarDisplayed: false,
    };
  },
  watch: {
    isDisplaySnackBar: function (value){
        if (value){
            this.isSnackBarDisplayed = true;
        }
    }
  }
};
</script>

<style>
</style>