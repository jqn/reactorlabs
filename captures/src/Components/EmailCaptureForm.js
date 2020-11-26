import React from "react";
import PropTypes from "prop-types";

import Form from "react-bootstrap/Form";
import FormControl from "react-bootstrap/FormControl";
import InputGroup from "react-bootstrap/InputGroup";
import Button from "react-bootstrap/Button";

const EmailCaptureForm = () => {
  return (
    <main className="form-email">
      <Form>
        <h2 className="h2 text-left mb-5">
          Would you like to get notified when I publish new content?
        </h2>
        <h4 className="h4 text-left mb-3">Get the latest sent to your inbox</h4>
        <InputGroup className="mb-3">
          <FormControl
            size="lg"
            placeholder="Enter email"
            aria-label="Enter email"
          />
          <InputGroup.Append>
            <Button size="lg" variant="outline-secondary">
              Submit
            </Button>
          </InputGroup.Append>
        </InputGroup>
      </Form>
    </main>
  );
};

EmailCaptureForm.defaultProps = {};

EmailCaptureForm.propTypes = {};

export default EmailCaptureForm;
