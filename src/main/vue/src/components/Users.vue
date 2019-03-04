<template>

  <div class="container">
    <div class="row">
            <div class="col-sm-10">
                      <h1>Login</h1>
              <table class="table table-hover">
                <thead>
                <tr>
                  <th scope="col">Username</th>
                  <th scope="col">Password</th>
                <th></th>
                </tr>
                </thead>
                  <tbody>
                    <td><input ref="loginname" placeholder="username"></td>
                    <td><input type="password" ref="loginpass" placeholder="password"></td>
                    <td><button type="button"
                                class="btn btn-primary btn-sm"
                                @click="login()">
                        Login
                        </button>
                    </td>
                  </tbody>
              </table>

            </div>
      <div class="col-sm-10">
        <h1>Users</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button"
                class="btn btn-success btn-sm"
                v-b-modal.user-modal
                v-if=show>
                Add User
        </button>
        <br><br>

        <!-- users table -->
        <table class="table table-hover ">
          <thead>
            <tr>
              <th scope="col">Image</th>
              <th scope="col">Username</th>
              <th scope="col">E-Mail</th>
              <th scope="col">Rights</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td><img :src="user.picture "
                                   class="rounded-circle" width="50" height="50"/></td>
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.admin }}</td>
              <td>
                <button type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.user-update-modal
                        v-if=show
                        @click="editUser(user)">
                    Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        v-if=show
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
            user="Add a new user"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-user-group"
                      label="User:"
                      label-for="form-user-input">
            <b-form-input id="form-user-input"
                          type="text"
                          v-model="addUserForm.username"
                          required
                          placeholder="Enter user">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-email-group"
                      label="E-Mail:"
                      label-for="form-email-input">
          <b-form-input id="form-email-input"
                        type="text"
                        v-model="addUserForm.email"
                        required
                        placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-picture-group"
                      label="Image:"
                      label-for="form-picture-input">
          <b-form-input id="form-picture-input"
                        type="text"
                        v-model="addUserForm.picture"
                        required
                        placeholder="Enter Image">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group"
                      label="Password:"
                      label-for="form-password-input">
          <b-form-input id="form-password-input"
                        type="password"
                        v-model="addUserForm.password"
                        required
                        placeholder="Enter Password">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-admin-group">
            <b-form-checkbox-group v-model="addUserForm.admin" id="form-checks">
              <b-form-checkbox value="true">Admin?</b-form-checkbox>
            </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editUserModal"
             id="user-update-modal"
             user="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-user-edit-group"
                      label="User:"
                      label-for="form-user-edit-input">
          <b-form-input id="form-user-edit-input"
                        type="text"
                        v-model="editForm.username"
                        required
                        placeholder="Enter user">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-email-edit-group"
                      label="E-Mail:"
                      label-for="form-email-edit-input">
          <b-form-input id="form-email-edit-input"
                        type="text"
                        v-model="editForm.email"
                        required
                        placeholder="Enter email">
          </b-form-input>
        </b-form-group>
         <b-form-group id="form-picture-edit-group"
                      label="Image:"
                      label-for="form-picture-edit-input">
          <b-form-input id="form-picture-edit-input"
                        type="text"
                        v-model="editForm.picture"
                        required
                        placeholder="Enter Image">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-edit-group"
                      label="Password:"
                      label-for="form-password-edit-input">
          <b-form-input id="form-password-edit-input"
                        type="password"
                        v-model="editForm.password"
                        required
                        placeholder="Enter password">
          </b-form-input>
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
        password: '',
        admin: false,
      },
      show: false,
      editForm: {
        username: '',
        email: '',
        picture: '',
        password: '',
        admin: '',
      },
      message: '',
      showMessage: false,
      uname: '',
      pass: '',
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getUsers() {
      const path = 'http://localhost:5000/users';
      axios.get(path, {
        auth: {
          username: this.uname,
          password: this.pass,
        },
      })
        .then((res) => {
          this.users = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUser(payload) {
      const path = 'http://localhost:5000/users';
      axios.post(path, payload, {
        auth: {
          username: this.uname,
          password: this.pass,
        },
      })
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
      const path = `https://eecevit-flask.herokuapp.com/users/${userID}`;
      axios.put(path, payload, {
        auth: {
          username: this.uname,
          password: this.pass,
        },
      })
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
      axios.delete(path, {
        auth: {
          username: this.uname,
          password: this.pass,
        },
      })
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
      this.addUserForm.username = '';
      this.addUserForm.email = '';
      this.addUserForm.picture = '';
      this.addUserForm.password = '';
      this.addUserForm.admin = false;
      this.editForm.username = '';
      this.editForm.email = '';
      this.editForm.picture = '';
      this.editForm.password = '';
      this.editForm.admin = false;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      const payload = {
        username: this.addUserForm.username,
        email: this.addUserForm.email,
        picture: this.addUserForm.picture,
        password: this.addUserForm.password,
        admin: this.addUserForm.admin,
      };
      this.addUser(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      const payload = {
        username: this.editForm.username,
        email: this.editForm.email,
        picture: this.editForm.picture,
        password: this.addUserForm.password,
        admin: this.addUserForm.admin,
      };
      this.updateUser(payload, this.editForm.username);
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
      this.removeUser(user.username);
    },
    editUser(user) {
      this.editForm = user;
    },
    login() {
      this.uname = '';
      this.pass = '';
      this.uname = this.$refs.loginname.value;
      this.pass = this.$refs.loginpass.value;
      this.getUsers();
      this.check();
    },
    check() {
      const path = `http://localhost:5000/user/${this.uname}`;
      axios.get(path)
        .then((res) => {
          if (res.data[0] === 'true') {
            this.show = true;
          } else {
            this.show = false;
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      // console.log(this.user.admin);
    },
  },
  created() {
    this.getUsers();
  },
};
</script>
