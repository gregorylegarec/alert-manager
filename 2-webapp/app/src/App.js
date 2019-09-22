import React from "react";
import { connect } from "react-redux";
import { Container, CircularProgress } from "@material-ui/core";
import AlertsTable from "./components/AlertsTable";

export class App extends React.Component {
  componentDidMount() {
    this.props.fetchAlerts();
  }

  render() {
    const { alerts, isLoading } = this.props;
    return (
      <Container p="16" width="100%">
        <h1>Alert Manager</h1>
        {isLoading ? (
          <CircularProgress mx="auto" />
        ) : (
          <AlertsTable alerts={alerts} />
        )}
      </Container>
    );
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
