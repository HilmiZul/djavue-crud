<template>
  <div class="students">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h2>
                Students
                <router-link to="/students/add/" class="btn btn-success">Add</router-link>
              </h2>
            </div>
            <div class="card-body">
              <div class="form-group">
                <input type="text" v-model="cari" class="form-control" placeholder="coba cari: Zul">
              </div>
              <table class="table table-striped table-hover">
                <thead>
                  <tr>
                    <th>NO.</th>
                    <th>NAMA</th>
                    <th>KELAS</th>
                    <th>STATUS</th>
                    <th>TANGGAL MASUK</th>
                    <th>POIN</th>
                    <th>TINDAKAN</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(student, index) in filterStudent" :key="student.id">
                    <td>{{ index+1 }}.</td>
                    <td><router-link :to="{ name: 'EditStudent', params: { id: student.id }}">{{ student.nama }}</router-link></td>
                    <td>{{ student.kelas }}</td>
                    <td>
                      <span v-if="student.status === true" class="badge badge-success">Aktif</span>
                      <span v-else class="badge badge-danger">Tidak Aktif</span>
                    </td>
                    <td>{{ student.tgl_masuk }}</td>
                    <td>{{ student.poin }}</td>
                    <td>
                      <!-- <button class="btn btn-danger" data-toggle="modal">Hapus</button> -->
                      <button class="btn btn-danger" v-on:click="hapus(student.id)">Hapus</button>
                    </td>
                    <!-- modal disini -->
                    <div class="modal">
                      <div class="modal-dialog">
                        <div class="modal-content">
                          <div class="modal-header">
                            Hapus?
                          </div>
                          <div class="modal-body">
                            Apa Anda yakin ingin menghapus data ini?
                          </div>
                          <div class="modal-footer">
                            <button class="btn btn-outline-danger">Hapus</button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </tr>
                </tbody>
              </table>
            </div> <!-- ./card-body -->
          </div> <!-- ./card -->
        </div> <!-- ./col-md-12 -->
      </div> <!-- ./row -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Students',
  data() {
    return {
      students: [],
      cari: ''
    }
  },

  // async created() {
  //   let response = await fetch('http://127.0.0.1:8000/api/students/');
  //   this.students = await response.json()
  // },
  mounted() {
    this.showStudents()
  },

  methods: {
    showStudents() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/students/',
      })
      .then(response => this.students = response.data)
    },

    hapus(id_student) {
      if (confirm("Hapus data ini?")) {
        axios({
          method: 'delete',
          url: 'http://127.0.0.1:8000/api/students/' + id_student
        })
        .then(res => {
          this.showStudents()
          // let index = this.students.indexOf(id_student)
          // this.students.splice(index, 1)
        })
      } // end if confirm
    } // end hapus()
  },

  computed: {
    filterStudent() {
      return this.students.filter(student => {
        return student.nama.toLowerCase().includes(this.cari.toLowerCase())
      })
    }
  }
}
</script>
