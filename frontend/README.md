# Heritage Site Health Monitoring - React Frontend

A modern, professional React application for AI-powered heritage site structural analysis.

## Features

- 🎨 **Beautiful UI/UX**: Professional gradient backgrounds, smooth animations, and glass morphism effects
- 🚀 **Fast & Responsive**: Optimized performance with React and Framer Motion animations
- 📊 **Interactive Visualizations**: Real-time charts and graphs using Recharts
- 🔄 **Real-time Processing**: Live progress tracking during image analysis
- 📱 **Mobile Responsive**: Works seamlessly on all devices
- 🎯 **Intuitive Navigation**: Easy-to-use sidebar and routing system

## Tech Stack

- **React 18.2** - Frontend framework
- **React Router 6** - Navigation and routing
- **Framer Motion** - Smooth animations and transitions
- **Recharts** - Data visualization charts
- **Axios** - HTTP client for API requests
- **Lucide React** - Beautiful icon library
- **React Dropzone** - Drag-and-drop file uploads

## Installation

### Prerequisites

- Node.js 16+ and npm installed
- Backend server running on `http://localhost:5000`

### Setup Instructions

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start development server**:
   ```bash
   npm start
   ```

4. **Open browser**:
   Navigate to `http://localhost:3000`

## Project Structure

```
frontend/
├── public/
│   └── index.html          # HTML template
├── src/
│   ├── components/         # Reusable components
│   │   ├── Header.js       # Navigation header
│   │   ├── Sidebar.js      # Sidebar navigation
│   │   └── ResultsDisplay.js  # Analysis results display
│   ├── pages/              # Page components
│   │   ├── HomePage.js     # Landing page
│   │   ├── AnalysisPage.js # Image analysis page
│   │   ├── EnvironmentalPage.js  # Environmental footprints
│   │   └── AboutPage.js    # About and features
│   ├── App.js              # Main app component
│   ├── App.css             # Global styles
│   ├── index.js            # Entry point
│   └── index.css           # Base styles
├── package.json            # Dependencies
└── README.md               # This file
```

## Features Overview

### 1. Home Page
- Hero section with call-to-action
- Feature cards showcasing capabilities
- Real-time statistics and metrics

### 2. Analysis Page
- Drag-and-drop image upload
- Real-time progress tracking
- Multiple analysis tabs:
  - Crack Detection with severity indicators
  - Segmentation results
  - Biological growth analysis
  - Depth estimation heatmaps
  - Edge detection
- Interactive charts and visualizations
- Downloadable PDF reports

### 3. Environmental Page
- Carbon footprint analysis
- Water footprint monitoring
- Material impact factors
- Sustainability tips

### 4. About Page
- Mission statement
- Key features showcase
- Technology stack overview
- Workflow explanation

## API Integration

The frontend connects to the Flask backend at `http://localhost:5000`

### Endpoints Used

- `GET /api/health` - Health check
- `POST /api/analyze` - Image analysis
- `POST /api/generate-pdf` - PDF report generation

## Customization

### Colors and Themes

Edit `src/App.css` and `src/index.css` to customize:
- Background gradients
- Button colors
- Card styles
- Animations

### Adding New Features

1. Create new component in `src/components/`
2. Add route in `src/App.js`
3. Style in corresponding `.css` file

## Build for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.

## Deployment

### Using Serve
```bash
npm install -g serve
serve -s build -p 3000
```

### Using Nginx
Copy `build/` contents to nginx web root and configure reverse proxy to backend.

## Troubleshooting

### Backend Connection Error
- Ensure Flask backend is running on port 5000
- Check CORS is enabled in backend
- Verify API endpoint URLs in components

### Image Upload Issues
- Check file size limits
- Ensure supported formats (JPG, PNG, JPEG)
- Verify backend has proper file handling

### Performance Issues
- Clear browser cache
- Check network tab for slow API calls
- Optimize images before upload

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

This project is part of the Heritage Site Health Monitoring system.

## Support

For issues and questions, please check the backend documentation or contact the development team.
