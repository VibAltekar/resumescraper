/**
 *
 * Search
 *
 */

import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { compose } from 'redux';

/* eslint-disable react/prefer-stateless-function */
export class Search extends React.Component {
  constructor(props) {
  	super(props);
  	this.state = {
  		query: "", 
  		results: []
  	}

  	this.changeQuery = this.changeQuery.bind(this);
  	this.buildSubmitButton = this.buildSubmitButton.bind(this); 
  	this.submitQuery = this.submitQuery.bind(this);
  }

  changeQuery(event) {
  	this.setState({
  		query: event.target.value
  	}, () => {
  		console.log("Query changed!");
  	});
  }

  submitQuery() {
  	var queryToSubmit = this.state.query; 
  	this.props.history.push("/search/".concat(queryToSubmit));
  }

  buildSubmitButton() {
  	return (
  		<button disabled={this.state.query === ""} onClick={this.submitQuery}>Search</button>
  	); 
  }

  buildSearchField() {
  	return (
  		<input type="text" value={this.state.query} onChange={this.changeQuery} placeholder={"Enter query"}/>
  	)
  }

  buildComponent() {
  	return (
  		<div>
  			{this.buildSearchField()}
  			{this.buildSubmitButton()}
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
