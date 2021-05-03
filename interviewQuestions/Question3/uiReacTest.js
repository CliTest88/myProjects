

//================react-dropdown-select Test==========================


import React from "react";
import {
  render,
  fireEvent,
  cleanup,
  waitForElement,
  getByText
} from "react-testing-library";


const MyDropdown = () => (
    <Dropdown
        data-testid="dropdown"
        options={options}
        defaultValue={options[0].value}
    />
);

// not sure if framwork need this function:

 before(function(done) {
    driver
      .navigate()
      .to("https://sanusart.github.io/react-dropdown-select/")
      .then(() => done());
  });

it('runs without crashing', () => {
    render(<MyDropdown />);
});

it('can change the value of the dropdown', () => {
    const { getByTestId } = render(<MyDropdown />);

    const dropdown = getByTestId('dropdown');

    const display = dropdown.children[0];

    expect(display.textContent).toBe(options[0].text);

    console.log(display.textContent);

    fireEvent.click(dropdown);

    const dropdownOptions = getAllByRole(dropdown, 'option');

    fireEvent.click(dropdownOptions[2]);

    expect(display.textContent).toBe(options[2].text);

    console.log(display.textContent);

 // fireEvent.change(selectInput, { target: { value: "Mellie Leannon"} });
 // await waitForElement(() => getByText(selectOutput, "Mellie Leannon"));
 // expect(screen.getByText("selected option name is ")).toBeInTheDocument();

   after(function(done) {
    driver.quit().then(() => done());
});




