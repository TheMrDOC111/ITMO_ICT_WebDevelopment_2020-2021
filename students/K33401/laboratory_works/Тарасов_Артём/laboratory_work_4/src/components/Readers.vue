<template>
  <div>
    <button @click="getReaders">Получить читателей</button>
    <v-simple-table class="v-data-table">
      <template v-slot:default class="theme--light">
        <thead>
        <tr>
          <th class="text-center">
            Full name
          </th>
          <th class="text-center">
            Phone
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="reader in readers" v-bind:key="reader.id">
          <td>
            <router-link :to="{name:'OneReader', params:{id: reader.id}}">{{ reader.full_name }}</router-link>
          </td>
          <td>{{ reader.phone }}</td>
          <td>
            <v-btn color="#ff0000" @click="deleteReader(reader.id)">Удалить</v-btn>
          </td>
        </tr>
        </tbody>
        <v-btn @click="createReader">Добавить читателя</v-btn>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import $ from 'jquery'

const baseUrlApi = 'http://127.0.0.1:8005/api/readers/'

export default {
  name: 'Readers',
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.getReaders()
  },
  data () {
    return {
      readers: ''
    }
  },
  methods: {
    /**
     * Function for getting all data
     */
    getReaders () {
      $.ajax({
        url: baseUrlApi,
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.readers = response
        },
        error: (response) => {
          alert('Пользователь не авторизован')
          console.log(response)
        }
      })
    },
    /**
     * Function for route to another component
     */
    createReader () {
      this.$router.push({ name: 'OneReader' })
    },
    /**
     * Function for delete data object
     * @param {number} id
     */
    deleteReader (id) {
      $.ajax({
        url: baseUrlApi + id + '/',
        type: 'DELETE',
        success: (response) => {
          alert('Готово')
          console.log(response)
          this.getReaders()
        },
        error: (response) => {
          alert('Пользователь не авторизован')
          console.log(response)
        }
      })
    }
  }

}
</script>

<style scoped>

</style>
