'use client';

import Link from 'next/link';
import { useSelector } from 'react-redux';

export default function Navbar() {
  const { user } = useSelector(state => state.auth);
  const { items } = useSelector(state => state.cart);

  return (
    <nav className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/" className="text-xl font-bold">E-commerce Store</Link>
        <div className="space-x-4">
          <Link href="/products">Products</Link>
          <Link href="/cart">Cart ({items.length})</Link>
          {user ? (
            <span>{user.username}</span>
          ) : (
            <>
              <Link href="/login">Login</Link>
              <Link href="/register">Register</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}