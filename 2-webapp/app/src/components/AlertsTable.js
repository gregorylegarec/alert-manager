import React from "react";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Paper
} from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
  root: {
    width: "100%",
    marginTop: theme.spacing(3),
    overflowX: "auto"
  },
  table: {
    minWidth: 650
  }
}));

export const AlertsTable = props => {
  const classes = useStyles();
  const { alerts } = props;

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <TableCell>Status</TableCell>
            <TableCell>Date</TableCell>
            <TableCell align="right">Score</TableCell>
            <TableCell align="right">Category</TableCell>
            <TableCell align="right">Client</TableCell>
            <TableCell align="right">Summary</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {alerts.map(alert => (
            <TableRow key={alert.id}>
              <TableCell component="th" scope="row">
                {alert.status}
              </TableCell>
              <TableCell component="th" scope="row">
                {alert.date}
              </TableCell>
              <TableCell component="th" scope="row">
                {`${alert.score}%`}
              </TableCell>
              <TableCell align="right">{alert.category}</TableCell>
              <TableCell align="right">{alert.client}</TableCell>
              <TableCell align="right">{alert.summary}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
};

export default AlertsTable;
