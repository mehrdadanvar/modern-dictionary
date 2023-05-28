<template>
  <div class="navbar">
    <v-app-bar :elevation="6" rounded>
      <div class="nav-holder">
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/lessons">lessons</NuxtLink>
      </div>
      <template v-slot:append>
        <v-btn icon="mdi-heart"></v-btn>
        <v-btn icon="mdi-magnify"></v-btn>
        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-app-bar>
  </div>
</template>

<script>
  export default {};
</script>

<style scoped>
  .nav-holder {
    display: flex;
    width: 20rem;
    gap: 1rem;
  }
</style>
