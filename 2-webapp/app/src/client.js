// This module is a decoy !
//
// It's actually just a mock which use an hard coded promise to simulate
// asynchronous access to API.

import fixtures from "./fixtures";

const SIMULATION_DELAY = 2000;

export const client = {
  async fetchAlerts() {
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(fixtures), SIMULATION_DELAY);
    });
  }
};

export default client;
