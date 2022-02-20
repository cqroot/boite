<template>
  <a-layout id="main-layout">
    <a-layout-sider id="sider" v-model="collapsed" collapsible>
      <div class="logo">
        {{ collapsed ? "B" : "Boite" }}
      </div>
      <a-menu theme="dark" mode="inline" :selectedKeys="[routeName]">
        <a-menu-item v-for="item in routes" :key="item.name">
          <router-link :to="item.path" tag="div">
            <a-icon :type="item.meta.icon" />
            <span>{{ item.name }}</span>
          </router-link>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>

    <a-layout>
      <a-layout-content
        class="main-content"
        :style="collapsed ? 'margin-left: 104px' : 'margin-left: 224px'"
      >
        <slot />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script>
import routes from "@/router/routes";

export default {
  computed: {
    routeName() {
      const name = this.$route.name;
      if (typeof name === "string") {
        return name;
      } else {
        return "";
      }
    },
  },
  data() {
    return {
      routes,
      collapsed: false,
    };
  },
};
</script>

<style lang="scss" scoped>
#main-layout {
  min-height: 100%;
}

#sider {
  overflow: auto;
  height: 100vh;
  position: fixed;
  left: 0;

  .logo {
    height: 32px;
    line-height: 32px;
    margin: 16px;
    color: white;
    font-weight: bold;
    font-size: 30px;
    text-align: center;
    margin-top: 30px;
    cursor: pointer;
    -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    -khtml-user-select: none;
    user-select: none;
  }
}

.main-content {
  margin-right: 24px;
  margin-top: 16px;
  margin-bottom: 16px;
  padding: 40px;
  background: #fff;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  position: fixed;
  overflow-y: auto;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

::-webkit-scrollbar {
  width: 7px;
  height: 7px;
}

::-webkit-scrollbar-corner {
  background: none;
}

::-webkit-scrollbar-track {
  border: none;
}

::-webkit-scrollbar-thumb {
  background: rgba(100, 100, 100, 0.3);
  border-radius: 5px;
}

::-webkit-scrollbar-track:hover {
  background: rgba(0, 0, 0, 0.1);
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(100, 100, 100, 0.7);
}
</style>
