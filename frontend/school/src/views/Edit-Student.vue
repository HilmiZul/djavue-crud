<template>
  <div class="add-students">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h2>
                Edit Students
                <router-link to="/students" class="btn btn-danger">Back</router-link>
              </h2>
            </div>
            <div class="card-body">
              <div class="col-md-6">
                <div class="alert alert-success" v-if="success">
                  Data Berhasil diperbaharui!
                </div>
                <form @submit.prevent="submitStudent()">
                  <div class="form-group">
                    <label class="label">NAMA</label>
                    <input type="text" class="form-control" v-model="student.nama" required="required">
                  </div>
                  <div class="form-group">
                    <label class="label">KELAS</label>
                    <select class="form-control" v-model="student.kelas" required="required">
                      <option >Pilih Kelas</option>
                      <option value="Python">Python</option>
                      <option value="Ruby">Ruby</option>
                      <option value="Vue.js">Vue.js</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label class="label">POIN</label>
                    <input type="number" class="form-control" v-model="student.poin" required="required">
                  </div>
                  <div class="form-group">
                    <label class="label">Status</label>
                    <input type="checkbox" class="form-control" v-model="student.status">
                  </div>
                  <button class="btn btn-success" :disabled="loading">
                    <span v-if="loading">
                      <Circle8></Circle8>
                    </span>
                    <span v-if="!loading">Simpan</span>
                  </button>
                </form>
              </div>
            </div> <!-- ./card-body -->
          </div> <!-- ./card -->
        </div> <!-- ./col-md-12 -->
      </div> <!-- ./row -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {Circle8} from 'vue-loading-spinner'

export default {
  name: 'Add-Students',
  data() {
    return {
      student: {
        'id': this.$route.params.id,
        'nama': '',
        'kelas': '',
        'poin': '',
        'status': '',
      },
      success: ''
    }
  },

  components: {
    Circle8
  },

  props: {
      loading: { type: Boolean }
  },

  mounted() {
    this.showStudent();
  },

  methods: {
    // tampilin data yg mau diedit ke form
    showStudent() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/students/' + this.$route.params.id + '/',
      }).then(response => this.student = response.data)
    },

    submitStudent() {
      if (this.$route.params.id) {
        this.editStudent();
      }
    },

    async editStudent() {
      // tampilin dulu data sebelum edit
      await this.showStudent();

      await fetch(`http://127.0.0.1:8000/api/students/`+this.$route.params.id+`/`,{
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      })

      // tampilkan perubahan
      this.showStudent()

      // ubah var success
      this.success = true
    }
  }
}
</script>
