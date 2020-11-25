import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/leads")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        console.log("🚀 ~ file: App.js ~ line 25 ~ App ~ .then ~ data", data);
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
  }

  render() {
    return <p>Hello World React!</p>;
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);

module.hot.accept();
