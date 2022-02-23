<template>
  <div id="page-unixtimestamp" class="page-content">
    <a-row>
      <a-col :span="7"
        ><div style="text-align: right; padding-right: 10px; line-height: 40px">
          Unix Timestamp:
        </div>
      </a-col>
      <a-col :span="5">
        <a-input style="height: 40px" v-model="timestampToConvert"></a-input>
      </a-col>
      <a-col :span="6" style="white-space: nowrap"
        ><a-button
          type="primary"
          style="height: 32px; width: 90px; margin: 0 10px"
          @click="timestampToTime"
        >
          convert
        </a-button>
        <a-input style="height: 40px" compact v-model="convertedTime"
      /></a-col>
    </a-row>
  </div>
</template>

<script>
import moment from "moment";

export default {
  name: "UnixTimestamp",
  data() {
    return {
      timestampToConvert: "",
      convertedTime: "",
    };
  },
  methods: {
    timestampToTime() {
      this.convertedTime = moment
        .unix(this.timestampToConvert)
        .format("YYYY-MM-DD hh:mm:ss");
    },
  },
};
</script>
