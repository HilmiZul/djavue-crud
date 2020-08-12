<template>
  <div id="app">
    <div id="nav">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <nav class="nav mt-3 mb-3">
              <router-link to="/" class="nav-link">Home</router-link>
              <router-link to="/students" class="nav-link">Students</router-link>
              <router-link to="/about" class="nav-link">About</router-link>
            </nav>
          </div>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';
</style>
