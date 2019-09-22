import React from "react";
import { connect } from "react-redux";

export class App extends React.Component {
  componentDidMount() {
    this.props.fetchAlerts();
  }
  render() {
    return <div></div>;
  }
}

const mapState = state => ({
  alerts: state.alerts,
  isLoading: state.loading.effects.alerts.fetchAlerts
});

const mapDispatch = ({ alerts: { fetchAlerts } }) => ({
  fetchAlerts
});

export default connect(
  mapState,
  mapDispatch
)(App);
