import React from 'react';
import { CreditCard } from 'lucide-react';

const Accounts = ({ accounts, accountForm, setAccountForm, handleCreateAccount }) => {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 animate-fade-in pb-10">

      <div className="lg:col-span-1">
         <div className="card bg-base-100 shadow-xl border border-base-200 sticky top-0">
            <div className="card-body">
               <h3 className="card-title text-lg font-black uppercase mb-4 flex items-center gap-2">
                   <CreditCard className="w-6 h-6 text-accent" /> Open Account
               </h3>
               <form onSubmit={handleCreateAccount} className="flex flex-col gap-4">
                  <div className="form-control w-full">
                     <label className="label"><span className="label-text font-bold text-xs uppercase opacity-60">Account ID</span></label>
                     <input type="number" className="input input-bordered w-full bg-base-200" value={accountForm.account_id} onChange={e => setAccountForm({...accountForm, account_id: e.target.value})} required />
                  </div>
                  <div className="form-control w-full">
                     <label className="label"><span className="label-text font-bold text-xs uppercase opacity-60">Owner Member ID</span></label>
                     <input type="number" className="input input-bordered w-full bg-base-200" value={accountForm.member_id} onChange={e => setAccountForm({...accountForm, member_id: e.target.value})} required />
                  </div>
                  <div className="form-control w-full">
                     <label className="label"><span className="label-text font-bold text-xs uppercase opacity-60">Initial Balance (KES)</span></label>
                     <input type="number" className="input input-bordered w-full bg-base-200" value={accountForm.balance} onChange={e => setAccountForm({...accountForm, balance: e.target.value})} required />
                  </div>
                  <button type="submit" className="btn btn-accent w-full mt-4 font-black tracking-widest">Open Account</button>
               </form>
            </div>
         </div>
      </div>

      {/* Accounts Table - Right Column */}
      <div className="lg:col-span-2">
         <div className="card bg-base-100 shadow-xl border border-base-200 h-full">
            <div className="card-body p-0">
               <div className="p-4 border-b border-base-200 flex items-center justify-between bg-base-200/30">
                  <h2 className="card-title text-base font-black uppercase tracking-tight">Accounts List</h2>
                  <div className="badge badge-accent badge-outline">{accounts.length} Active</div>
               </div>
               <div className="overflow-x-auto">
                  <table className="table table-zebra w-full">
                     <thead className="bg-base-200/50 text-xs font-black uppercase opacity-60">
                        <tr>
                           <th>ID</th>
                           <th>Owner</th>
                           <th className="text-right">Balance</th>
                        </tr>
                     </thead>
                     <tbody>
                        {accounts.map(a => (
                          <tr key={a.account_id}>
                             <th className="font-mono text-accent">#{a.account_id}</th>
                             <td>Member <span className="font-mono font-bold">{a.member_id}</span></td>
                             <td className="text-right font-bold text-success">KES {a.balance.toLocaleString()}</td>
                          </tr>
                        ))}
                        {accounts.length === 0 && <tr><td colSpan="3" className="text-center py-8 opacity-50">No records found</td></tr>}
                     </tbody>
                  </table>
               </div>
            </div>
         </div>
      </div>
    </div>
  );
};

export default Accounts;