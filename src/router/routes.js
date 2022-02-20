const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/HomeView.vue"),
    meta: { icon: "user" },
  },
  {
    path: "/bytecalc",
    name: "ByteCalc",
    component: () => import("../views/ByteCalc.vue"),
    meta: { icon: "calculator" },
  },
];

export default routes;
