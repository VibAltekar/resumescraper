/**
 *
 * Search
 *
 */

import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { compose } from 'redux';
import "../../components/app.css";

/* eslint-disable react/prefer-stateless-function */
export class Search extends React.Component {
  constructor(props) {
  	super(props);
  	this.state = {
  		query: (this.props.match.params.query === undefined) ? "" : this.props.match.params.query,
  		results: []
  	}
  	this.changeQuery = this.changeQuery.bind(this);
  	this.submitQuery = this.submitQuery.bind(this);
  }

  changeQuery(event) {
  	this.setState({
  		query: event.target.value
  	}, () => {
      this.submitQuery();
  		console.log("Query changed!");
  	});
  }

  submitQuery() {
  	var queryToSubmit = this.state.query;
    console.log("pushing new view");
  	this.props.history.push("/search/".concat(queryToSubmit));
  }

  buildSearchField() {
  	return (
  		<input type="text" value={this.state.query} onChange={this.changeQuery} placeholder={"Enter query"}/>
  	)
  }

  buildComponent() {
    console.log("hi", this.props.match.params);

  	return (
  		<div>
  			{this.buildSearchField()}
  		</div>
  	)
  }

  render() {
    return (
    	<div>
    		{this.buildComponent()}
    	</div>
    );
  }
}


Search.propTypes = {
  dispatch: PropTypes.func.isRequired,
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

export default compose(withConnect)(Search);
