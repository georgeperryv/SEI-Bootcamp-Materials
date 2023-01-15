import { useState, useEffect } from 'react';
import * as ordersAPI from '../../utilities/orders-api'
import UserLogOut from '../../components/UserLogOut/UserLogOut';
import OrderDetail from '../../components/OrderDetail/OrderDetail';
import OrderList from '../../components/OrderList/OrderList';

export default function OrderHistoryPage({ user, setUser }) {
  const [orders, setOrders] = useState([])
  // const [selectedOrder, setSelectedOrder] = useState(null)

  useEffect(function () {
    async function getOrders() {
      const orders = await ordersAPI.getOrderForUser()
      // console.log(orders)
      setOrders(orders);

    }
    getOrders();
  }, [])

  return (
    <>
      <h1>OrderHistoryPage</h1>

      <OrderList
        orders={orders}
      />

      {/* <OrderDetail order={selectedOrder} /> */}

      <UserLogOut user={user} setUser={setUser} />
    </>
  );
}