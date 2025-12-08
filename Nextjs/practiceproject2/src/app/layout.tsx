import type { Metadata } from "next";
import "./globals.css";


export const metadata: Metadata = {
  title: "Auth Project",
  description: "Auth Project with next js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
