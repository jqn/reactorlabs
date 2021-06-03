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
        <h2 className="text-left mb-4 display-6 fw-normal">
          Would you like to get notified when we publish new content?
        </h2>
        <p className="h4 text-left mb-4 fw-normal">Get the latest sent to your inbox</p>
        <div className="col-lg-12 mx-auto px-0">
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
        </div>
      </Form>
    </main>
  );
};

EmailCaptureForm.defaultProps = {};

EmailCaptureForm.propTypes = {};

export default EmailCaptureForm;
