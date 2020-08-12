<template>
  <div class="add-students">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h2>
                Students &raquo; Add New
                <router-link to="/students" class="btn btn-danger">Back</router-link>
              </h2>
            </div>
            <div class="card-body">
              <div class="col-md-6">
                <div class="alert alert-success" v-if="success">
                  Data Berhasil disimpan!
                </div>
                <form @submit.prevent="addStudent">
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
                  <button class="btn btn-success" :disabled="loading">
                    <span v-if="loading">
                      <rotate-square2></rotate-square2>
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
import {RotateSquare2} from 'vue-loading-spinner'

export default {
  name: 'Add-Students',
  data() {
    return {
      student: {
        'nama': '',
        'kelas': '',
        'poin': '',
      },
      success: ''
    }
  },

  components: {
    RotateSquare2
  },

  props: {
      loading: { type: Boolean }
  },

  methods: {
    addStudent() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/students/',
        data: {
          nama: this.student.nama,
          kelas: this.student.kelas,
          poin: this.student.poin,
        }
      }).then((response) => {
        let newStudent = {
          'id': response.data.id,
          'nama': this.nama,
          'kelas': this.kelas,
          'poin': this.poin,
        }
        this.success = true
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
