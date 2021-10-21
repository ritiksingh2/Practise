import "tailwindcss/tailwind.css";
import { userProvider } from "../context/userContext";
function MyApp({ Component, pageProps }) {
  return (
    <userProvider>
      <Component {...pageProps} />
    </userProvider>
  );
}

export default MyApp;
