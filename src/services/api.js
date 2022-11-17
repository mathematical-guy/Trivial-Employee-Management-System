import axios from "axios";
import { BASE_URL, urls } from "./constants";

function getEmployeesList() {
  return axios.get(`${BASE_URL}/${urls.employeeListURL}`)
}

function updateEmployeeAPI(id, payload) {
  return axios.patch(`${BASE_URL}/${urls.employeeDetailURL}/${id}`, payload)
}


function fetchEmployeeAPI(id) {
  return axios.get(`${BASE_URL}/${urls.employeeDetailURL}/${id}`)
}

function createEmployeeAPI(payload) {
  return axios.post(`${BASE_URL}/${urls.employeeDetailURL}`, payload)
}

function deleteEmployeeAPI(id) {
  return axios.delete(`${BASE_URL}/${urls.employeeDetailURL}/${id}`)
}


export {
  getEmployeesList,
  updateEmployeeAPI,
  fetchEmployeeAPI,
  createEmployeeAPI,
  deleteEmployeeAPI
};


