BEGIN;

-- Subjects
INSERT INTO subjects (name) VALUES
  ('Mathematics'),
  ('Physics'),
  ('Chemistry'),
  ('Computer Science');

-- Categories (assuming IDs: Math=1, Physics=2, Chemistry=3, CS=4)
INSERT INTO categories (name, subject_id) VALUES
  -- Mathematics
  ('Algebra', 1),
  ('Geometry', 1),
  ('Calculus', 1),
  ('Probability', 1),

  -- Physics
  ('Mechanics', 2),
  ('Optics', 2),
  ('Thermodynamics', 2),

  -- Chemistry
  ('Organic Chemistry', 3),
  ('Inorganic Chemistry', 3),
  ('Physical Chemistry', 3),

  -- Computer Science
  ('Algorithms', 4),
  ('Data Structures', 4),
  ('Databases', 4);

-- Tasks (assuming categories are numbered sequentially)
INSERT INTO tasks (question, answer, category_id) VALUES
  -- Algebra
  ('Solve x^2 - 4x + 4 = 0', 'x=2', 1),
  ('Factorize x^2 - 9', '(x-3)(x+3)', 1),

  -- Geometry
  ('Area of circle with r=7', '≈153.94', 2),
  ('Volume of cube with side=3', '27', 2),

  -- Calculus
  ('Derivative of cos(x)', '-sin(x)', 3),
  ('Integral of 2x dx', 'x^2 + C', 3),

  -- Probability
  ('Probability of rolling a 6 on a fair die', '1/6', 4),
  ('Expected value of coin toss (heads=1, tails=0)', '0.5', 4),

  -- Mechanics
  ('Force on 5kg mass with a=2m/s^2', '10N', 5),
  ('Work done by 20N force over 3m', '60J', 5),

  -- Optics
  ('Speed of light in vacuum', '3×10^8 m/s', 6),
  ('Lens with focal length 0.25m has power?', '4 diopters', 6),

  -- Thermodynamics
  ('First law of thermodynamics', 'ΔU = Q - W', 7),
  ('Absolute zero in Celsius', '-273.15°C', 7),

  -- Organic Chemistry
  ('Functional group in CH3-COOH', 'Carboxyl group', 8),
  ('Name of C2H5OH', 'Ethanol', 8),

  -- Inorganic Chemistry
  ('Formula of sodium chloride', 'NaCl', 9),
  ('Oxidation state of Fe in Fe2O3', '+3', 9),

  -- Physical Chemistry
  ('Ideal gas law equation', 'PV = nRT', 10),
  ('pH of neutral solution at 25°C', '7', 10),

  -- Algorithms
  ('Time complexity of bubble sort', 'O(n^2)', 11),
  ('Binary search complexity', 'O(log n)', 11),

  -- Data Structures
  ('Stack principle', 'LIFO', 12),
  ('Queue principle', 'FIFO', 12),

  -- Databases
  ('SQL command to select all rows from table users', 'SELECT * FROM users;', 13),
  ('Primary key definition', 'Unique identifier for a row', 13);

COMMIT;
