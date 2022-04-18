<template>
  <div id="page-bytecalc" class="page-content">
    <a-row
      v-for="item in byteData"
      :key="item.name"
      style="margin-bottom: 10px; height: 40px"
    >
      <a-col :span="7">
        <div style="text-align: right; padding-right: 10px; line-height: 40px">
          {{ item.text }}:
        </div>
      </a-col>
      <a-col :span="12">
        <a-input
          v-model="item.value"
          style="height: 40px"
          @change="inputChange(item.name, item.value)"
          @pressEnter="calculate(item.name, item.value)"
        />
      </a-col>
    </a-row>

    <a-row>
      <a-col :span="7"></a-col>
      <a-col :span="12">
        <a-button
          type="primary"
          style="margin-right: 10px"
          @click="calculate(currentUnit, currentValue)"
        >
          Calculate
        </a-button>
        <a-button @click="clear"> Clear</a-button>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentUnit: "",
      currentValue: "",
      byteData: [
        {
          name: "bit",
          text: "bit (b)",
          value: "",
        },
        {
          name: "byte",
          text: "byte (B)",
          value: "",
        },
        {
          name: "kilobyte",
          text: "kilobyte (kB)",
          value: "",
        },
        {
          name: "megabyte",
          text: "megabyte (MB)",
          value: "",
        },
        {
          name: "gigabyte",
          text: "gigabyte (GB)",
          value: "",
        },
        {
          name: "terabyte",
          text: "terabyte (TB)",
          value: "",
        },
      ],
    };
  },
  methods: {
    inputChange(name, value) {
      this.currentUnit = name;
      this.currentValue = value;
    },
    calculate(name, value) {
      value = value.replace(/[, ]/g, "");
      console.log(value);
      switch (name) {
        case "bit":
          break;
        case "byte":
          value *= 8;
          break;
        case "kilobyte":
          value *= 8192;
          break;
        case "megabyte":
          value *= 8388608;
          break;
        case "gigabyte":
          value *= 8589934592;
          break;
        case "terabyte":
          value *= 8796093022208;
          break;
        default:
      }
      let data = {
        bit: value,
        byte: value / 8,
        kilobyte: value / 8192,
        megabyte: value / 8388608,
        gigabyte: value / 8589934592,
        terabyte: value / 8796093022208,
      };
      this.byteData.forEach((item) => {
        item.value = data[item.name];
      });
    },
    clear() {
      this.byteData.forEach((item) => (item.value = ""));
    },
  },
};
</script>
