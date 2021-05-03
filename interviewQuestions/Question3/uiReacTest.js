



//================react-dropdown-select Test==========================


import React from "react";
import {
  render,
  fireEvent,
  cleanup,
  waitForElement,
  getByText
} from "react-testing-library";
import App from "./App";

afterEach(cleanup);

const setup = () => {
  const utils = render(<App />);
  const selectOutput = utils.getByTestId("select-output");
  const selectInput = document.getElementById("react-select-2-input");
  return { selectOutput, selectInput };
};

test("it can change selected item", async () => {
  const { selectOutput, selectInput } = setup();
  getByText(selectOutput, "Shanahan Mill");
  fireEvent.change(selectInput, { target: { value: "Mellie Leannon"} });
  await waitForElement(() => getByText(selectOutput, "Mellie Leannon"));
  expect(screen.getByText("selected option name is ")).toBeInTheDocument();
});

