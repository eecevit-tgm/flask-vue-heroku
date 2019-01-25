<template>
  <div class="User">
    <div class="read">
      <form>
          <input type="text" name="username" placeholder="Username">
          <input type="text" name="email" placeholder="E-Mail">
          <input type="text" name="Image" placeholder="Image-Link">
          <input type="submit" value="Submit">

      </form>
    </div>
    <div class="table">
      <table>
          <thead>
            <th>username</th>
            <th>email</th>
            <th>image</th>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid lightgray" v-for="(user, index) in Users" :key="index">
              <td>{{user.username}}</td>
              <td>{{user.email}}</td>
              <td>{{user.picture}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    <h2>User</h2>
    <div class="table">
      <table class="table table-hover">
          <thead>
            <th>username</th>
            <th>email</th>
            <th>image</th>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid lightgray" v-for="(user, index) in User" :key="index">
              <td>{{user.username}}</td>
              <td>{{user.email}}</td>
              <td>{{user.picture}}</td>
              <td>
                <button type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.user-update-modal
                        @click="editUser(user)">
                    Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteUser(user)">
                    Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>


    <-- Edit Form Beginn-->
    <b-modal ref="editUserModal"
             id="user-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group"
                      label="Title:"
                      label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-username-edit-group"
                      label="Username:"
                      label-for="form-username-edit-input">
          <b-form-input id="form-user-edit-input"
                        type="text"
                        v-model="editForm.user"
                        required
                        placeholder="Enter username">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-mail-edit-group"
                      label="E-Mail:"
                      label-for="form-mail-edit-input">
          <b-form-input id="form-mail-edit-input"
                        type="text"
                        v-model="editForm.mail"
                        required
                        placeholder="Enter E-Mail">
          </b-form-input>
        </b-form-group>
          <b-form-group id="form-image-edit-group"
                      label="Image:"
                      label-for="form-image-edit-input">
          <b-form-input id="form-image-edit-input"
                        type="text"
                        v-model="editForm.image"
                        required
                        placeholder="Enter Image">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>

    </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
        Users: [],
        User:[],
      editForm: {
        username: '',
        mail: '',
        image: '',
      },
      message: '',
      showMessage: false,
    };
  },

  methods:{
  getUsers () {
      axios.get("http://127.0.0.1:5000/users").then(res =>{
        this.Users = res.data
      })
  },
  getUser() {
    axios.get("http://127.0.0.1:5000/users/eecevit ").then(res => {
      this.User = res.data
    })
  },
      updateUser(username) {
      const path = `http://localhost:5000/books/${username}`;
      axios.put(path)
        .then(() => {
          this.getUsers();
          this.message = 'User updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUser();
        });
    },
    removeUser(username) {
      const path = `http://localhost:5000/books/${username}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'User removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUsers();
        });

    },
    editUser(user) {
      this.editForm = user;
    },
     onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      let read = false;
      const payload = {
        user: this.editForm.username,
        author: this.editForm.mail,
        price: this.editForm.image,
      };
      this.updateUser(this.editForm.username);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      this.initForm();
      this.getUsers(); // why?
    }
  },
  created() {
    this.getUsers()
    this.getUser()
  }
};
</script>


<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
