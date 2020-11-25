import React, { Component } from "react";
import { render } from "react-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import EmailCaptureForm from "./Components/EmailCaptureForm";

class App extends Component {
  // constructor(props) {
  //   super(props);
  //   this.state = {
  //     data: [],
  //     loaded: false,
  //     placeholder: "Loading",
  //   };
  // }

  // componentDidMount() {
  //   fetch("http://127.0.0.1:8000/api/leads")
  //     .then((response) => {
  //       if (response.status > 400) {
  //         return this.setState(() => {
  //           return { placeholder: "Something went wrong!" };
  //         });
  //       }
  //       return response.json();
  //     })
  //     .then((data) => {
  //       console.log("🚀 ~ file: App.js ~ line 25 ~ App ~ .then ~ data", data);
  //       this.setState(() => {
  //         return {
  //           data,
  //           loaded: true,
  //         };
  //       });
  //     });
  // }

  render() {
    return <EmailCaptureForm />;
  }
}

export default App;
