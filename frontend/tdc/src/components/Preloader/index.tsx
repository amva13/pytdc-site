import React, { useEffect } from "react";
import { loader } from "../../utils";
import { Helmet } from "react-helmet";

const PreloaderContainer: React.FC = () => {
  useEffect(() => {
    loader();
  }, []);

  return (
    <>
      <Helmet>
        <meta charSet="utf-8" />
        <meta name="robots" content="noindex, follow" />
        <meta
          name="description"
          content="Hope – Health &amp; Medical React JS Template"
        />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1, shrink-to-fit=no"
        />
      </Helmet>
      <div id="preloader">
        <div className="preload-content">
          <div id="dream-load"></div>
        </div>
      </div>
    </>
  );
};

export default PreloaderContainer;
