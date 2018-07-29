/**
 *
 * Query
 *
 */

import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { compose } from 'redux';

/* eslint-disable react/prefer-stateless-function */
export class Query extends React.Component {
  constructor(props) {
  	super(props);
  	this.state = {
  		results: [],
  		query: this.props.match.params.query
  	}
  }
  render() {
    return <div>{this.state.query}</div>;
  }
}

Query.propTypes = {
  dispatch: PropTypes.func.isRequired
};

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
  };
}

const withConnect = connect(
  null,
  mapDispatchToProps,
);

export default compose(withConnect)(Query);
