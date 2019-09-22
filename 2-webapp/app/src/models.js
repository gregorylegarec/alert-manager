import client from "./client";

export const alerts = {
  state: [],
  reducers: {
    receive(state, payload = []) {
      return payload;
    }
  },
  effects: dispatch => ({
    // No parameter, but if we want to filter alerts this function will
    // soon take filter parameters.
    async fetchAlerts() {
      const alerts = await client.fetchAlerts();
      dispatch.alerts.receive(alerts);
    }
  })
};
