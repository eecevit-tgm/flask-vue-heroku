<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>User</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.user-modal>Add User</button>
        <br><br>

        <!-- users table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Username</th>
              <th scope="col">E-Mail</th>
              <th scope="col">Image</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td>{{ user.username }}</td>
              <td>{{ user.email}}</td>
              <td>${{ user.image }}</td>
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
    </div>

    <!-- add user modal -->
    <b-modal ref="addUserModal"
             id="user-modal"
            title="Add a new user"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title:"
                      label-for="form-title-input">
            <b-form-input id="form-title-input"
                          type="text"
                          v-model="addUserForm.username"
                          required
                          placeholder="Enter title">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addUserForm.email"
                        required
                        placeholder="Enter author">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-price-group"
                      label="Purchase price:"
                      label-for="form-price-input">
          <b-form-input id="form-price-input"
                        type="number"
                        v-model="addUserForm.image"
                        required
                        placeholder="Enter price">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

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
                        v-model="editForm.username"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                        type="text"
                        v-model="editForm.email"
                        required
                        placeholder="Enter author">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-price-edit-group"
                      label="Purchase price:"
                      label-for="form-price-edit-input">
          <b-form-input id="form-price-edit-input"
                        type="number"
                        v-model="editForm.image"
                        required
                        placeholder="Enter price">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';
export default {
  data() {
    return {
      users: [],
      addUserForm: {
        username: '',
        email: '',
        image: '',
      },
      editForm: {
        username: '',
        email: '',
        image: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getUsers() {
      const path = 'http://localhost:5000/users';
      axios.get(path)
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUser(payload) {
      const path = 'http://localhost:5000/users';
      axios.post(path, payload)
        .then(() => {
          this.getUsers();
          this.message = 'User added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUsers();
        });
    },
    updateUser(payload, userID) {
      const path = `http://localhost:5000/users/${userID}`;
      axios.put(path, payload)
        .then(() => {
          this.getUsers();
          this.message = 'User updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUsers();
        });
    },
    removeUser(userID) {
      const path = `http://localhost:5000/users/${userID}`;
      axios.delete(path)
        .then(() => {
          this.getUsers();
          this.message = 'User removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUsers();
        });
    },
    initForm() {
      this.addUserForm.title = '';
      this.addUserForm.author = '';
      this.addUserForm.read = [];
      this.addUserForm.price = '';
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
      this.editForm.id = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      let read = false;
      if (this.addUserForm.read[0]) read = true;
      const payload = {
        title: this.addUserForm.title,
        author: this.addUserForm.author,
        read, // property shorthand
        price: this.addUserForm.price,
      };
      this.addUser(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read, // property shorthand
        price: this.editForm.price,
      };
      this.updateUser(payload, this.editForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      this.initForm();
      this.getUsers(); // why?
    },
    onDeleteUser(user) {
      this.removeUser(user.id);
    },
    editUser(user) {
      this.editForm = user;
    },
  },
  created() {
    this.getUsers();
  },
};
</script>
