import Link from 'next/link';
import Navbar from '@/components/Navbar';



export default function Home() {
  return (
    <div>
      <Navbar />
      <main className="container mx-auto mt-8">
        <h1 className="text-4xl font-bold mb-4">Welcome to Our E-commerce Store</h1>
        <p className="mb-4">Find the best products at great prices!</p>
        <Link href="/products" className="bg-blue-500 text-white px-4 py-2 rounded">
          Shop Now
        </Link>
      </main>
    </div>
  );
}