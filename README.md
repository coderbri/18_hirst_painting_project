# 18 Hirst Painting Project

## Overview

This project is the **Day 18 Challenge** of the **100 Days of Code: Python Pro Bootcamp** by Dr. Angela Yu. The challenge focuses on modularizing code and using external Python libraries, specifically **colorgram** and **turtle**, to recreate a digital version of Damien Hirst's famous *Spot Painting*.


## Table of Contents

- Key Features
- Project Setup
   - [1. Install Dependencies](#1-install-dependencies)
   - [2. Add Input Image](#2-add-input-image)
   - [3. Extract Colors](#3-extract-colors)
   - [4. Recreate the Artwork](#4-recreate-the-artwork)


## Key Features

1. **Extracting Colors**: Utilize the **colorgram** library to extract a palette of colors from an image.
2. **Creating Artwork**: Use the **turtle** module to generate a grid of colored dots inspired by Hirst’s art.
3. **Modular Design**: Split functionalities across multiple Python files for better organization.



## Project Setup

### 1. Install Dependencies

- Install the **colorgram** package from PyPI using:
  ```bash
  pip install colorgram.py
  ```

- The **turtle** module is a standard library in Python and does not require installation.

### 2. Add Input Image

- Download an image of your choice (e.g., **image.jpg**) and place it in the project directory.

### 3. Extract Colors

- Create a file named **color_extraction.py** to extract colors from the image:

   ```python
   import colorgram

   colors = colorgram.extract('image.jpg', 30)  # Extract 30 colors
   rgb_colors = []
   for color in colors:
      r = color.rgb.r
      g = color.rgb.g
      b = color.rgb.b
      rgb_colors.append((r, g, b))

   print(rgb_colors)
   ```

- Example output when running this script in the terminal:

   ```bash
   [<colorgram.py Color: Rgb(r=249, g=249, b=249), 78.44117638183134%>, 
   <colorgram.py Color: Rgb(r=248, g=246, b=247), 12.710869577400791%>, 
   <colorgram.py Color: Rgb(r=224, g=229, b=236), 3.1572399111751444%>, ...]
   ```

- The terminal output displays a list of Color objects containing RGB values and additional data. To access just the RGB values:

   ```python
   rgb_colors = []
   for color in colors:
      rgb_colors.append(color.rgb)
   print(rgb_colors)
   ```

- Result:

   ```bash
   [Rgb(r=249, g=249, b=249),
   Rgb(r=248, g=246, b=247),
   Rgb(r=224, g=229, b=236), ...]
   ```


- Extract the individual red (`r`), green (`g`), and blue (`b`) components and save them as tuples for easier use:

   ```python
   rgb_colors = []
   for color in colors:
      r = color.rgb.r
      g = color.rgb.g
      b = color.rgb.b
      new_color = (r, g, b)
      rgb_colors.append(new_color)
   print(rgb_colors)
   ```

- Final output: `[(249, 249, 249), (248, 246, 247), (224, 229, 236), ...]`

- Save this `color_list` in **color_extraction.py** for reuse in the next steps.


### 4. Recreate the Artwork

In **main.py**, logic is implemented to recreate the painting using the **turtle** module.

#### 1. Set Up the Turtle Environment:

- Import the turtle module and configure it to use RGB color mode with `turtle_module.colormode(255)`.

- Create a turtle object (tim) and adjust its speed, visibility, and position.

   ```python
   tim = turtle_module.Turtle()
   tim.speed("fastest")
   tim.penup()
   tim.hideturtle()
   tim.setheading(225)
   tim.forward(300)
   tim.setheading(0)
   ```

#### 2. Draw the Dots:

- Use a loop to draw the specified number of dots (`number_of_dots`), selecting a random color from the `color_list` for each dot.

- Ensure the turtle moves forward after each dot.

   ```python
   for dot_count in range(1, number_of_dots + 1):
      tim.dot(20, random.choice(color_list))
      tim.forward(50)
   ```

#### 3. Handle Row Transitions:

- After every 10 dots, reposition the turtle to start a new row.

   ```python
   if dot_count % 10 == 0:
      tim.setheading(90)
      tim.forward(50)
      tim.setheading(180)
      tim.forward(500)
      tim.setheading(0)
   ```

#### 4. Finalize and Display:

- Set up the screen to exit upon a mouse click, allowing the user to view the completed artwork.

   ```python
   screen = turtle_module.Screen()
   screen.exitonclick()
   ```



## Additional Notes

- **Damien Hirst Inspiration**: This project’s grid-based design mimics Hirst’s abstract use of colorful dots.
- **Turtle Module**: The **turtle** module is used to render graphics on the screen, enabling the creation of the dot grid.
- **Modularization**: By separating color extraction and painting logic into different files, the project remains organized and easy to expand.
- **Customization**: The painting size and dot colors can be customized by changing the `number_of_dots` or the extracted `color_list`.


---
<section align="center">
  <code>coderBri © 2024</code>
</section>