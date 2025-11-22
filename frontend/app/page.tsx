import Navbar from "@/components/Navbar";
import { HeroSection } from "@/components/home/HeroSection";
import { LatestInsights } from "@/components/home/LatestInsights";
import { Newsletter } from "@/components/home/Newsletter";
import { Footer } from "@/components/Footer";

export default function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground selection:bg-foreground selection:text-background">
      <Navbar />
      <HeroSection />
      <LatestInsights />
      <Newsletter />
      <Footer />
    </div>
  );
}
