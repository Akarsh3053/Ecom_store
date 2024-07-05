'use client';

import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useRouter } from 'next/navigation';
import api from '@/utils/api';
import Navbar from '@/components/navBar';
// import Navbar from '@/components/Navbar';

export default function Checkout() {
  const [address, setAddress] = useState('');
  const { items } = useSelector(state => state.cart);
  const dispatch = useDispatch();
  const router = useRouter();

  const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/orders/', { address, items });
      // Clear cart and redirect to order confirmation page
      // You'll need to implement the clearCart action in your cartSlice
      dispatch(clearCart());
      router.push('/order-confirmation');
    } catch (error) {
      console.error('Checkout failed:', error);
    }
  };

  return (
    <div>
      <Navbar />
      <main className="container mx-auto mt-8">
        <h1 className="text-2xl font-bold mb-4">Checkout</h1>
        <form onSubmit={handleSubmit} className="max-w-md">
          <div className="mb-4">
            <label htmlFor="address" className="block mb-2">Shipping Address</label>
            <textarea
              id="address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
              className="w-full px-3 py-2 border rounded"
              rows="3"
            ></textarea>
          </div>
          <div className="mb-4">
            <h2 className="text-xl font-semibold">Order Summary</h2>
            {items.map((item) => (
              <div key={item.id} className="flex justify-between">
                <span>{item.name} x {item.quantity}</span>
                <span>${(item.price * item.quantity).toFixed(2)}</span>
              </div>
            ))}
            <div className="font-bold mt-2">
              Total: ${total.toFixed(2)}
            </div>
          </div>
          <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded">
            Place Order
          </button>
        </form>
      </main>
    </div>
  );
}