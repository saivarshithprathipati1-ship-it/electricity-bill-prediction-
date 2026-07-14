# Electricity Bill Prediction Frontend

Modern React TypeScript frontend for the Electricity Bill Prediction AI Agent.

## Features

- 🔮 **Bill Prediction**: Get accurate predictions based on consumption patterns
- 📊 **Analysis Dashboard**: View seasonal factors and regional pricing
- 💡 **Energy Tips**: Get personalized energy-saving recommendations
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- ⚡ **Fast Performance**: Built with React 18 and TypeScript
- 🎨 **Modern UI**: Beautiful gradient backgrounds and smooth interactions

## Prerequisites

- Node.js 16+ and npm/yarn
- Backend API running on `http://localhost:8000`

## Installation

```bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test
```

## Project Structure

```
src/
├── pages/
│   ├── HomePage.tsx          # Landing page
│   ├── PredictionPage.tsx    # Bill prediction form and results
│   ├── AnalysisPage.tsx      # Seasonal and regional analysis with charts
│   └── TipsPage.tsx          # Energy saving tips
├── components/
│   ├── Navbar.tsx            # Navigation bar
│   ├── Card.tsx              # Reusable card component
│   └── LoadingSpinner.tsx    # Loading indicator
├── services/
│   └── api.ts                # API service with axios
├── types/
│   └── index.ts              # TypeScript type definitions
├── App.tsx                   # Main app component with routing
└── index.tsx                 # Entry point
```

## API Integration

The frontend communicates with the backend API at `http://localhost:8000`. Ensure the backend is running before starting the frontend.

### Environment Variables

Create a `.env` file in the frontend directory:

```
REACT_APP_API_URL=http://localhost:8000
```

## Usage

### Home Page
Welcome page with feature overview and quick links to prediction and analysis.

### Prediction Page
1. Enter consumption units (kWh)
2. Select month and region
3. Choose customer type (residential, commercial, or industrial)
4. Click "Get Prediction" to receive:
   - Predicted bill amount
   - Confidence score
   - Consumption analysis
   - Personalized recommendations

### Analysis Page
- View seasonal adjustment factors across all months
- See regional pricing differences
- Analyze consumption patterns

### Tips Page
- Get energy-saving recommendations
- Learn about benefits of energy conservation
- Practical tips organized by category

## Technologies Used

- **React 18**: UI framework
- **TypeScript**: Type-safe JavaScript
- **React Router v6**: Client-side routing
- **Axios**: HTTP client for API calls
- **Recharts**: Data visualization
- **Tailwind CSS**: Utility-first CSS (via custom styles)
- **React Icons**: Icon library

## Styling

The project uses a custom CSS approach with CSS modules and utility classes:

- Color scheme defined in `index.css`
- Component-specific styles in `.css` files
- Responsive design with mobile-first approach
- Smooth animations and transitions

## Build and Deploy

```bash
# Build for production
npm run build

# The build output will be in the /dist directory
# Deploy the contents to your hosting platform
```

## Troubleshooting

### API Connection Errors
- Ensure the backend API is running on `http://localhost:8000`
- Check if CORS is properly configured in the backend
- Verify the `REACT_APP_API_URL` environment variable

### Build Errors
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Check Node.js version compatibility
- Ensure all TypeScript types are properly defined

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT
