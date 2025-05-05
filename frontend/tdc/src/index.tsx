import React, { useEffect } from 'react';
import Head from 'next/head';
import dynamic from 'next/dynamic';

const App = dynamic(() => import('./App'), { ssr: false }); // Dynamically import App to ensure client-side rendering

const Home: React.FC = () => {
  useEffect(() => {
    const rootElement = document.getElementById('root');
    if (!rootElement) {
      console.error("Root element not found. Make sure there's a div with id 'root'.");
    }
  }, []);

  return (
    <>
      {/* Head component for metadata */}
      <Head>
        <meta property="og:title" content="PyTDC: The Commons" />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://tdcommons.ai" />
        {/* Uncomment and provide a valid image URL if needed */}
        {/* <meta property="og:image" content="mymainimage.jpg" /> */}
      </Head>

      {/* Main App Component */}
      <App />
    </>
  );
};

export default Home;
