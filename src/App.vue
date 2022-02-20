<template>
  <div id="app">
    <MainLayout>
      <router-view />
    </MainLayout>
  </div>
</template>

<script>
import MainLayout from "@/components/layouts/MainLayout.vue";

export default {
  name: "App",
  components: {
    MainLayout,
  },
};
</script>

<style lang="scss" scoped>
#app {
  height: 100%;
}
</style>
