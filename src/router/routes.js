const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/HomeView.vue"),
    meta: { icon: "user" },
  },
  {
    path: "/bytecalc",
    name: "Byte Calc",
    component: () => import("../views/ByteCalc.vue"),
    meta: { icon: "calculator" },
  },
  {
    path: "/unixtimestamp",
    name: "Unix Timestamp",
    component: () => import("../views/UnixTimestamp.vue"),
    meta: { icon: "clock-circle" },
  },
];

export default routes;
