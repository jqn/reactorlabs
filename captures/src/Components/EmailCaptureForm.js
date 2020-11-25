import React from "react";
import PropTypes from "prop-types";

import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import FormControl from "react-bootstrap/FormControl";
import InputGroup from "react-bootstrap/InputGroup";
import Button from "react-bootstrap/Button";

const EmailCaptureForm = () => {
  return (
    <Container className="p-3">
      <Form>
        <InputGroup className="mb-3">
          <FormControl
            placeholder="Enter email"
            aria-label="Enter email"
            aria-describedby="basic-addon2"
          />
          <InputGroup.Append>
            <Button variant="outline-secondary">Submit</Button>
          </InputGroup.Append>
        </InputGroup>
      </Form>
    </Container>
  );
};

EmailCaptureForm.defaultProps = {};

EmailCaptureForm.propTypes = {};

export default EmailCaptureForm;
