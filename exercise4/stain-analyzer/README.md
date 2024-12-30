# Stain Area Analyzer

An Angular-based application for computing the area of a stain in binary images using Monte Carlo sampling method. This project was developed as part of a technical assessment.

## Features

- Upload and process binary images (white stain on black background)
- Generate random sampling points for area estimation
- Real-time area calculation using Monte Carlo method
- Results history table with filtering and sorting capabilities
- Step-by-step methodology explanation using carousel
- Responsive design using Angular Material and Tailwind CSS

## Project Structure

```
stain-analyzer/
├── src/
│   ├── app/
│   │   ├── components/
│   │   │   ├── stain-calculator/
│   │   │   └── results-table/
│   │   ├── services/
│   │   │   └── stain.service.ts
│   │   ├── models/
│   │   │   └── stain-result.model.ts
│   │   └── app.component.ts
│   └── styles.css
```

## Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)
- Angular CLI (v16 or higher)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/stain-analyzer.git
cd stain-analyzer
```

2. Install dependencies:

```bash
npm install
```

3. Install required Angular packages:

```bash
npm install @angular/material @angular/cdk @angular/animations
```

## Development Setup

1. Start the development server:

```bash
ng serve
```

2. Navigate to `http://localhost:4200/` in your browser. The application will automatically reload if you change any source files.

## Core Components

### Stain Calculator Component

- Handles image upload and display
- Implements Monte Carlo sampling logic
- Provides interactive slider for sample size selection
- Real-time area calculation

### Results Table Component

- Displays calculation history
- Provides sorting and filtering capabilities
- Responsive design for various screen sizes

### Services

#### Stain Service

- Manages image processing logic
- Handles random point generation
- Calculates area estimation
- Maintains calculation history

## State Management

The application uses Angular Signals for state management, providing:

- Reactive updates
- Efficient change detection
- Type-safe state management
- Predictable data flow

## Technical Implementation

### Area Calculation Method

The stain area is calculated using the Monte Carlo method:

1. Generate n random points within image boundaries
2. Count points falling inside the stain (white pixels)
3. Calculate area ratio: (points inside stain) / (total points)
4. Multiply by total image area for final result

### Image Processing

- Accepts binary images (white stain on black background)
- Validates image format and content
- Processes image data using HTML5 Canvas

## Testing

Run unit tests:

```bash
ng test
```

## Building for Production

Generate a production build:

```bash
ng build --prod
```

The build artifacts will be stored in the `dist/` directory.

## Technologies Used

- Angular 16+
- Angular Material
- Tailwind CSS
- TypeScript
- RxJS
- HTML5 Canvas API

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name] - Initial work

## Acknowledgments

- Angular team for the excellent framework
- Material Design team for the UI components
- The technical assessment team for the interesting challenge
