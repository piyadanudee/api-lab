# api-lab
| Characteristic | Blocks | Values in the tests | Test Cases |
|---|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 | `test_stars_out_of_range` (0, 6); `test_base_choice_is_saved` (3) |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field | `test_base_choice_is_saved` (3); `test_stars_decimal`; `test_stars_text`; `test_stars_missing` |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 | `test_base_choice_is_saved`; `test_pizza_does_not_exist` |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short | `test_base_choice_is_saved`; `test_no_token`; `test_token_wrong_length` |
